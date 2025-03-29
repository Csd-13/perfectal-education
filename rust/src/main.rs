use actix_web::{App, HttpServer};

mod api;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("Starting Perfectal Education Rust Backend...");

    HttpServer::new(|| {
        App::new()
            .configure(api::routes::configure_routes)
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
