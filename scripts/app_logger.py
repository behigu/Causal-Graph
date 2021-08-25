import logging

#Create and configure logger
logging.basicConfig(filename="../log/causallogs.log",
                    format='%(asctime)s %(message)s',
                    filemode='w',
                    level=logging.DEBUG,
                   )

logger = logging.getLogger()
