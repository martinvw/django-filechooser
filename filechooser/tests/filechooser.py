from django.test import TestCase
from filechooser import FileChooser

class FileChooserTestCase(TestCase):
    ID = 'tEsTIdEnTiFiEr'
    PATH = '/tmp'

    def setUp(self):
        self.filechooser = FileChooser(self.ID, self.PATH, None)


    def test_filechooser_url_pattern_name(self):
        """Validate whether the url pattern has the correct name"""
        pattern = self.filechooser.url_pattern()

        #self.assertEqual(pattern.callback, FileChooser.process)
        self.assertEqual(pattern.name, 'filechooser_' + self.ID)


    def test_filechooser_url_pattern_resolve(self):
        """Validate whether the url pattern matches the url and parameters correctly"""
        pattern = self.filechooser.url_pattern()

        ajax_list_path = pattern.resolve('filechooser/tEsTIdEnTiFiEr/ajax/list/')
        self.assertTrue(ajax_list_path)
        self.assertEqual(ajax_list_path.kwargs['type'], 'ajax')
        self.assertEqual(ajax_list_path.kwargs['method'], 'list')
        self.assertEqual(ajax_list_path.kwargs['file'], '')

        http_process_path = pattern.resolve('filechooser/tEsTIdEnTiFiEr/http/process/test.txt')
        self.assertTrue(http_process_path)
        self.assertEqual(http_process_path.kwargs['type'], 'http')
        self.assertEqual(http_process_path.kwargs['method'], 'process')
        self.assertEqual(http_process_path.kwargs['file'], 'test.txt')


    def test_filechooser_url_pattern_resolve_false(self):
        """Validate whether the url pattern does match urls which it should not"""
        pattern = self.filechooser.url_pattern()

        false_paths = {
            'filechooser/some_other_identifier/ajax/list/', # wrong identifier
            'filechooser/some_other_identifier/http/process/', # wrong identifier
            'filechooser/tEsTIdEnTiFiEr/https/list/', # wrong type
            'filechooser/tEsTIdEnTiFiEr/https/process/', # wrong type
            'filechooser/tEsTIdEnTiFiEr/ajax/non_existing/', # wrong method
            'filechooser/tEsTIdEnTiFiEr/http/non_existing/', # wrong method
        }

        for path in false_paths:
            self.assertFalse(pattern.resolve(path))


def callback_for_test(filename):
    pass
