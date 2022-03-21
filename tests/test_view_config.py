def test_config_ui(CONFIG_SCREEN):
    CONFIG_SCREEN.create_ui_content()
    instance_dir = dir(CONFIG_SCREEN)

    assert "log_path_box" in instance_dir
    assert "save_path_box" in instance_dir
    assert "yes_button" in instance_dir
    assert "no_button" in instance_dir
