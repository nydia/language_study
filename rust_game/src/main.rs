use bevy::prelude::*;

struct GamePlugin;

impl Plugin for GamePlugin {
    fn build(&self, app: &mut App) {
        app.add_startup_system(setup.system())
            .add_system(movement.system());
    }
}

fn setup(mut commands: Commands, asset_server: Res<AssetServer>) {
    // 添加背景、玩家角色等
}

fn movement(keys: Res<Input<KeyCode>>, mut query: Query<&mut Transform>) {
    // 实现玩家控制逻辑
}

fn main() {
    App::build()
        .add_plugins(DefaultPlugins)
        .add_plugin(GamePlugin)
        .run();
}