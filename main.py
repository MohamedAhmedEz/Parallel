from Data.Shared import SharedList
from parsers.redditFetcher import redditFetcher
from parsers.twitterFetcher import twitterFetcher

lst = SharedList()

twi = redditFetcher(lst)
twi.Parse()
lst.print_all()

