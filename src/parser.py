#import to zmapReporter
#parse banner outputs to dataframes


class Parser:

    def __init__(self, working_dir_path):
        self.working_dir = working_dir_path

    def load_banners(self):
        '''
        Load banner json files generated from zgrab

        returns: loaded banners
        '''
    
    def parse_banners(self):
        '''
        Parse loaded banners to pandas dataframes with select features

        returns: dict of dataframes
        '''

