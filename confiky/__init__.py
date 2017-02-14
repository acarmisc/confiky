import os
import ConfigParser

class ConfikySection:
    pass


class Confiky:

    def __init__(self, files=(), required_sections=list()):
        cfile = files or './settings.ini'
        config = ConfigParser.SafeConfigParser()
        config.optionxform = str

        if not isinstance(cfile, list):
            cfile = [cfile]

        self.files = cfile
        self.file_count = len(cfile)
        self.sections = list()

        for f in cfile:
            try:
                config.read(f)
            except Exception, e:
                raise ValueError('Unable to find settings.ini file in the root folder and no custom file path provided.')

            self.config = config

            sections = required_sections or config.sections()

            for section in sections:
                if not hasattr(self, section):
                    setattr(self, section, ConfikySection)
                
                el = getattr(self, section)
                self.sections.append(section)
                el.__dict__.update(config.items(section))
    
            self.sections = list(set(self.sections))

    def __repr__(self):
        if self.file_count == 1:
            return "<Confiky for %s>" % self.files[0]

        return "<Confiky for %s files>" % self.file_count

    def validate(self, sections=list(), fields=list()):
        """ Check if provided sections or fields is present in 
        the configuration object """
        sections_found = 0
        fields_found = 0
        all_found = False
        
        if sections and isinstance(sections, list):
            for s in sections:
                if hasattr(self, s):
                    sections_found += 1

            if sections_found == len(sections):
                section_all = True

        if fields and isinstance(fields, list):
            for f in fields:
                if hasattr(self, f):
                    fields_found += 1

            if fields_found == len(fields):
                fields_all = True

        if section_all and fields_all:
            all_found = True

        return dict(fields_found=fields_found, sections_found=sections_found, all_found=all_found)


    def is_valid(self, sections=list(), fields=list()):
        if self.validate(sections=sections, fields=fields):
            return True
    
        return False

    def explain(self):
        ddict = dict()
        for s in self.sections:
            csection = getattr(self, s)
            ddict[s] = csection.__dict__

        return ddict


if __name__ == '__main__':
    c = Confiky(files=['settings.ini', 'config.ini'])
    print c
    print c.files
    print c.sections
    print c.explain()
