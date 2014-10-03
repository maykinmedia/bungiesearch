from bungiesearch.aliases import SearchAlias

from core.models import Article, NoUpdatedField


class SearchTitle(SearchAlias):
    def alias_for(self, title):
        return self.search_instance.query('match', title=title)

    class Meta:
        models = (Article,)
        alias_name = 'title_search'

class Title(SearchAlias):
    def alias_for(self, title):
        return self.search_instance.query('match', title=title)

class InvalidAlias(SearchAlias):
    class Meta:
        models = (Article,)

class TitleFilter(SearchAlias):
    def alias_for(self, title):
        return self.search_instance.filter('term', title=title)

class NonApplicableAlias(SearchAlias):
    def alias_for(self, title):
        return self.search_instance.filter('term', title=title)

    class Meta:
        models = (NoUpdatedField,)
