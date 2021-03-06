from scraping.art_of_war import ArtOfWar
from scraping.website_scraper import WebsiteScraper
from scraping.project_gutenberg import ProjectGutenberg

class TestScraping:
    def test_website_scraper_url_default(self):
        ws = WebsiteScraper(None)
        assert ws.get_request_raw_text(None) is None

    def test_website_scraper_set_url(self):
        ws = WebsiteScraper(None)
        ws.set_url('test_url')
        assert ws.url == 'test_url'

    def test_aow_scraper_is_proper_subclass(self):
        aow = ArtOfWar()
        aow.set_url('test_url')
        assert aow.url == 'test_url'

    def test_pg_scraper_is_proper_subclass(self):
        pg = ProjectGutenberg()
        pg.set_url('test_url')
        assert pg.url == 'test_url'

    def test_pg_scraper_no_book_error_handling(self):
        pg = ProjectGutenberg()
        assert pg.search_text('query') == None
