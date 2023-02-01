class DocumentInfos:

    title = u'Algorithme de FFT'
    first_name = 'Luca'
    last_name = 'Charlier'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Février'
    seminary_title = u'Travail personnel OCI'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/LucaCharlier/FFT_Luca_Charlier"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()