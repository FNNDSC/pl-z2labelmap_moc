
from unittest import TestCase
from unittest import mock
from z2labelmap_moc.z2labelmap_moc import Z2labelmap_moc


class Z2labelmap_mocTests(TestCase):
    """
    Test Z2labelmap_moc.
    """
    def setUp(self):
        self.app = Z2labelmap_moc()

    def test_run(self):
        """
        Test the run code.
        """
        args = []
        if self.app.TYPE == 'ds':
            args.append('inputdir') # you may want to change this inputdir mock
        args.append('outputdir')  # you may want to change this outputdir mock

        # you may want to add more of your custom defined optional arguments to test
        # your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        options = self.app.parse_args(args)
        self.app.run(options)

        # write your own assertions
        self.assertEqual(options.outputdir, 'outputdir')
