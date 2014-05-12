# -*- coding: utf-8 -*-
"""
@Author: Karol Duleba

Allow specifing article type
Based on SubCategory plugin by Alistair Magee
"""

from operator import attrgetter
from functools import partial

from pelican import signals
from pelican.urlwrappers import URLWrapper


class PostType(URLWrapper):
    pass


def get_posttypes(generator, metadata):
    if 'POSTTYPE_SAVE_AS' not in generator.settings:
        generator.settings['POSTTYPE_SAVE_AS'] = 'type/{slug}/index.html'
    if 'POSTTYPE_URL' not in generator.settings:
        generator.settings['POSTTYPE_URL'] = 'type/{slug}/'

    def_posttype = generator.settings.get('DEFAULT_POSTTYPE', "post")

    posttype_name = metadata.get('posttype', def_posttype).strip()
    posttype = PostType(posttype_name, generator.settings)
    metadata['posttype'] = posttype


def create_posttypes(generator):
    generator.posttypes = []
    for article in generator.articles:
        posttype = [item for item in generator.posttypes
                    if item[0].name == article.posttype.name]

        if posttype:
            posttype[0][1].append(article)
        else:
            posttype = PostType(article.posttype.name, generator.settings)
            generator.posttypes.append((posttype, [article]))


def generate_posttype(generator, writer):
    write = partial(writer.write_file,
                    relative_urls=generator.settings['RELATIVE_URLS'])

    posttype_template = generator.get_template('posttype')

    for posttype, articles in generator.posttypes:
        articles.sort(key=attrgetter('date'), reverse=True)
        dates = [article for article in generator.dates if article in articles]

        write(name=posttype.save_as,
              template=posttype_template,
              context=generator.context,
              posttype=posttype,
              articles=articles,
              dates=dates,
              paginated={'articles': articles, 'dates': dates},
              page_name=posttype.page_name,
              all_articles=generator.articles)


def generate_posttype_feeds(generator, writer):
    for posttype, articles in generator.posttypes:
        articles.sort(key=attrgetter('date'), reverse=True)

        if generator.settings.get('POSTTYPE_FEED_ATOM'):
            path = generator.settings['POSTTYPE_FEED_ATOM'] % posttype.slug
            writer.write_feed(elements=articles,
                              context=generator.context,
                              path=path,
                              feed_type='atom')

        if generator.settings.get('POSTTYPE_FEED_RSS'):
            path = generator.settings['POSTTYPE_FEED_RSS'] % posttype.slug
            writer.write_feed(elements=articles,
                              context=generator.context,
                              path=path,
                              feed_type='rss')


def generate(generator, writer):
    generate_posttype_feeds(generator, writer)
    generate_posttype(generator, writer)


def register():
    signals.article_generator_context.connect(get_posttypes)
    signals.article_generator_finalized.connect(create_posttypes)
    signals.article_writer_finalized.connect(generate)
