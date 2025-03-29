pub struct AIModel {
    pub name: String,
    pub version: String,
}

impl AIModel {
    pub fn new(name: &str, version: &str) -> Self {
        AIModel {
            name: name.to_string(),
            version: version.to_string(),
        }
    }

    pub fn switch_model(&self) {
        println!("Switching to AI model: {} v{}", self.name, self.version);
    }
}
