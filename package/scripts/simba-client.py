from resource_management import *

class SimbaClient(Script):
    
    def install(self, env):
        import params
        Directory([params.simba_dir],
              mode=0755,
              cd_access='a',
              create_parents=True
        )
        Execute('cd ' + params.simba_dir + '; wget '+params.download_url+' -O simba.tar.gz; tar -xzf simba.tar.gz; rm -rf simba.tar.gz')

if __name__ == "__main__":
    SimbaClient().execute()