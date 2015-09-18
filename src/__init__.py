from src.crawler import FSCrawler

__author__ = 'marcin'

def main():
    crawler = FSCrawler()
    index = crawler.build_index("/Users/marcin/tmp")
    duplicates = crawler.get_duplicates(index)
    print(duplicates)

main()