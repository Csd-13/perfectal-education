use actix_web::{web, HttpResponse, Responder, Scope};
use crate::api::handlers::hello;

pub async fn switch_ai_model(model_name: web::Path<String>) -> impl Responder {
    HttpResponse::Ok().body(format!("Switched to AI model: {}", model_name))
}

pub fn configure_routes(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::scope("/api")
            .route("/hello", web::get().to(hello))
            .service(
                web::resource("/switch_ai_model/{model_name}")
                    .route(web::get().to(switch_ai_model)),
            ),
    );
}
