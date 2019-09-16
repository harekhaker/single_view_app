import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'single_view.settings')
django.setup()

from music_api.models import Music, Contributor, Provider
import pandas as pd
from fuzzywuzzy import process

def get_iniciales(name):
    return set([i[0] for i in name.split(' ')])

def remove_duplicate_names(contributors):
    o = set()
    for name in contributors.keys():
        l = []
        for a in process.extract(name, contributors):
            a = list(a)
            iniciales_main = get_iniciales(name)
            iniciales_checked = get_iniciales(a[0])
            if len(iniciales_main) == len(iniciales_checked) and a[1] >= 70:
                if iniciales_main == iniciales_checked:
                    a[1] += 15
                else:
                    a[1] -= 25
            l.append(a)
        o.add(max([i for i, b in l if b > 85], key=len))
    return list([contributors[k] for k in o])


def process_contribs(contributors):

    if len(contributors) >= 2:
        return list(remove_duplicate_names(contributors))
    else:
        return contributors.value()

def get_contribs(unit):
    contributors = dict()
    for contributor in set('|'.join(unit['contributors'].unique()).split('|')):
        contributors.update({contributor: Contributor(name=contributor)})
        for c in Contributor.objects.filter(name__trigram_similar=contributor):
            contributors.update({c.name: c})
    return process_contribs(contributors)


def get_sources(unit):
    sources = []
    for source in unit['source'].unique():
        source = source.strip().lower()
        s = list(Provider.objects.filter(name=source))
        if s:
            sources.append(Provider(name = source))
        else:
            sources+=s
    return sources


def main(file_path):
    df = pd.read_csv(file_path, sep=",")  # Normalize total_bedrooms column

    for iswc in list(df['iswc'].unique()):
        unit = df[df['iswc'] == iswc]

        music = list(Music.objects.filter(iswc=iswc))
        if music:
            music= Music(iswc=iswc).save()
        else:
            music = music[0]

        for contributor in get_contribs(unit):
            contributor.save()
            music.contributors.add(contributor)

        for source in get_sources(unit):
            source.save()
            music.providers.add(source)


        #TODO: bulk commit as example:
        # @transaction.commit_manually
        # def manual_transaction():
        #     for record in Record.objects.all():
        #         record.name = "String without number"
        #         record.save()
        #     transaction.commit()

        music.save()






# c = [Contributor(name='a'), Contributor(name='b'),]
# # c3 = []
# # for c2 in c:
# #     a = c2.save()
# #     c3.append(a)
# a = Music(song_name = 'youuuuu')
# a.save()
# for c1 in c:
#     c1.save()
#     a.contributors.add(c)
# a.save()
# # a.contributors.add(c).save()
#
#
#
#
#
#
#
#
#
#
# pprint(list(Music.objects.filter(iswc='1EFLM3K4MFL')))

