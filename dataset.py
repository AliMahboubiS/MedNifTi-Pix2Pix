import os
import sys
import logging

logger = logging.getLogger(__name__)  # logger
logger.setLevel(logging.INFO)


def _init_logger(flags, log_path):
    if flags.is_train:
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
        # file handler
        file_handler = logging.FileHandler(os.path.join(log_path, 'dataset.log'))
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        # stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        # add handlers
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)


class SpineC2M(object):
    def __init__(self, flags):
        self.flags = flags
        self.name = 'day2night'
        self.image_size = (256, 256, 1)
        self.num_tests = 7872

        # tfrecord path
        self.train_tfpath = os.path.abspath("pix2pix_db/tfrecords/train.tfrecords")
        self.test_tfpath = os.path.abspath("pix2pix_db/tfrecords/test.tfrecords")

        logger.info('Initialize {} dataset SUCCESS!'.format(self.flags.dataset))
        logger.info('Img size: {}'.format(self.image_size))

    def __call__(self, is_train='True'):
        if is_train:
            if not os.path.isfile(self.train_tfpath):
                sys.exit(' [!] Train tfrecord file is not found...')
            return self.train_tfpath
        else:
            if not os.path.isfile(self.test_tfpath):
                #sys.exit(' [!] Test tfrecord file is not found...')
                continue_param = 1
            return self.test_tfpath


# noinspection PyPep8Naming
def Dataset(dataset_name, flags, log_path=None):
    if flags.is_train:
        _init_logger(flags, log_path)  # init logger

    if dataset_name == 'pix2pix_db':
        return SpineC2M(flags)
    else:
        raise NotImplementedError
