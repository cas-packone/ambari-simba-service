from resource_management.libraries.script.script import Script

config = Script.get_config()
simba_dir=config['configurations']['simba']['home_dir']
download_url=config['configurations']['simba']['download_url']
