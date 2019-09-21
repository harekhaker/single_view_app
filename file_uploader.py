import os
from googletrans import Translator
import pandas as pd
from fuzzywuzzy import process
import numpy

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'single_view.settings')
django.setup()

from music_api.models import Music, Contributor, Source, Title


def process_titles(unit):
    title_pairs = dict()
    exist_titles = list()
    translator = Translator()
    for title in unit['title'].unique():
        if list(Title.objects.filter(title=title)):
            exist_titles.append(Title.objects.get(title=title))

        else:
            title_pair = dict()
            lang = translator.detect(title).lang
            title_pair.update({lang : dict()})
            title_pair[lang]['title'] = title
            title_pair[lang]['translation'] = translator.translate(title).text
            if title_pairs.get(lang):
                if title_pairs.get(lang)['translation'] == title_pair[lang]['translation']:
                    title_pairs.update(title_pair)
            else:
                title_pairs.update(title_pair)
    new_titles = list([Title(title=v['title'], lang=k, translation=v['translation']) for k, v in title_pairs.items()])

    return new_titles + exist_titles

def get_iniciales(name):
    return set([i[0] for i in name.split(' ')])

def remove_duplicate_names(contributors):
    o = set()
    for name in contributors.keys():
        if name != '':
            l = []
            for a in process.extract(name, contributors.keys()):
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
        for c in Contributor.objects.filter(name__contains=contributor):
            contributors.update({c.name: c})
    return process_contribs(contributors)


def get_sources(unit):
    sources = []
    for source in unit['source'].unique():
        source = source.strip().lower()
        s = list(Source.objects.filter(name=source))
        if s:
            sources += s
        else:
            sources.append(Source(name=source))
    return sources


def process_file(file):
    df = pd.read_csv(file, sep=",")

    for iswc in list(df['iswc'].unique()):
        if numpy.isnan(iswc):
            continue

        unit = df[df['iswc'] == iswc]

        music = list(Music.objects.filter(iswc=iswc))
        if music:
            music = music[0]
        else:
            music = Music(iswc=iswc)
            music.save()


        for title in process_titles(unit):
            title.save()
            music.titles.add(title)

        for contributor in get_contribs(unit):
            contributor.save()
            music.contributors.add(contributor)

        for source in get_sources(unit):
            source.save()
            music.sources.add(source)

        music.save()

        #TODO: bulk commit @transaction.commit_manually
