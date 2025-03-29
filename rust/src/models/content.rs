use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct Content {
    pub id: i32,
    pub title: String,
}
