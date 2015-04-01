import json

from django.test import TestCase
from filechooser.filechooser import FileChooser

from django.http import HttpResponse, HttpResponseNotFound

class FileChooserTestCase(TestCase):
    ID = 'tEsTIdEnTiFiEr'
    PATH = '.'

    def setUp(self):
        self.filechooser = FileChooser(self.ID, self.PATH, callback_for_test)


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


    def test_filechooser_process_list(self):
        """Validate whether the processing of a list works"""
        result_json = self.filechooser.process(None, '', 'ajax', 'list').content.decode('utf8')

        result = json.loads(result_json)
        self.assertTrue(result_json)
        self.assertTrue(result['data'])
        self.assertEqual(result['data'][0]['order'], 'a.git')
        self.assertEqual(result['data'][0]['filename']['display'], '.git')
        self.assertEqual(result['data'][0]['filename']['type'], 'folder')
        self.assertEqual(result['data'][0]['size']['display'], '-')
        self.assertTrue(result['data'][0]['mtime'])


    def test_filechooser_process_process(self):
        """Validate whether the processing of a process request works"""
        result = self.filechooser.process(None, '','http', 'process')

        self.assertEqual(result, 'some_unique_info_from_callback')


    def test_filechooser_process_false(self):
        """Validate whether the processing of incorrect requests is correctly handled"""
        result_wrong_combination = self.filechooser.process(None, '', 'http', 'list')

        self.assertIsInstance(result_wrong_combination, HttpResponseNotFound)

        result = None
        with self.assertRaises(EnvironmentError) as cm:
             result = self.filechooser.process(None, '../../', 'ajax', 'list')

        exception = cm.exception
        self.assertFalse(result)
        self.assertEquals(str(exception), 'Do not try to escape from the designated folder')



def callback_for_test(filename):
    return 'some_unique_info_from_callback'
