import logging
from executefeed1.feed1result import Feed1Result
logger = logging.getLogger("dealer")

class NoChoice(Feed1Result):

    def execute_feed1(self, can_feed_deque, dealer, index):
        logger.info("No choice")



    def __eq__(self, other):
        return isinstance(other, NoChoice)