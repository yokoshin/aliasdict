# -*- coding: utf-8 -*-
from unittest import TestCase

from io import BytesIO

from aliasdict import AliasDict


class TestAliasDict(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic_operation(self):
        e = AliasDict()

        self.assertFalse("key_a" in e)
        e["key_a"] = "value_a"
        self.assertEqual("value_a", e["key_a"])
        self.assertTrue("key_a" in e)

        e.set_alias("key_a", "key_b")
        self.assertEqual("value_a", e["key_b"])

        self.assertTrue("key_b" in e)
        self.assertFalse("key_c" in e)

        with self.assertRaises(KeyError):
            _ = e["key_c"]

    def test_len(self):
        e = AliasDict()
        e["key_a"] = "value_a"
        self.assertEqual(1, len(e))

    def test_composite_key(self):
        e = AliasDict()
        e["key_a"] = "value_a"
        self.assertEqual(1, len(e))

    def test_composite_key(self):
        e = AliasDict()
        e[("key_a", "key_b")] = "value_a"
        self.assertEqual("value_a", e[("key_a", "key_b")])

    def test_del_key0(self):
        e = AliasDict()
        e["key_a"] = "value_a"
        e["key_b"] = "value_b"

        del e["key_a"]
        self.assertEqual(1, len(e))

    def test_del_key1(self):
        e = AliasDict()
        e["key_a"] = "value_a"
        e.set_alias("key_a", "key_x")
        e.set_alias("key_a", "key_y")
        self.assertEqual(2, len(e.alias))
        self.assertEqual(1, len(e.ralias))

        del e["key_a"]
        self.assertEqual(0, len(e.alias))
        self.assertEqual(0, len(e.ralias))

    def test_del_key2(self):
        e = AliasDict()
        e["key_a"] = "value_a"
        e.set_alias("key_a", "key_x")
        e.set_alias("key_a", "key_y")
        self.assertEqual(2, len(e.alias))
        self.assertEqual(1, len(e.ralias))

        del e["key_x"]
        del e["key_y"]
        self.assertEqual(0, len(e.alias))
        self.assertEqual(0, len(dict(filter(lambda a: len(a[1]) > 0, e.ralias.items()))))


    def test_data_loading(self):
        e = AliasDict()
        e["key_a"] = "value_a"
        e["key_b"] = "value_b"
        e.set_alias("key_a", "alias_a")

        e2 = AliasDict(e.data)
        self.assertEqual("value_a", e2["key_a"])
        self.assertEqual("value_a", e2["alias_a"])

    def test_print(self):
        e = AliasDict()
        e["key_a"] = "value_a"
        e["key_b"] = "value_b"
        self.assertEqual("{'key_a': 'value_a', 'key_b': 'value_b'}", e.__str__())

    def test_dump_load(self):
        a = AliasDict()
        a["key_a"] = "value_a"
        a.set_alias("key_a", "alias_a")
        sio_in = BytesIO()
        a.dump(sio_in)

        sio_in.seek(0)
        b = AliasDict.load(sio_in)
        self.assertEqual("value_a", b["alias_a"])

    def test_dumps_loads(self):
        a = AliasDict()
        a["key_a"] = "value_a"
        a.set_alias("key_a", "alias_a")
        b = AliasDict.loads(a.dumps())
        self.assertEqual("value_a", b["alias_a"])


    def test_iterator(self):
        a = AliasDict()
        a["key_a"] = "value_a"
        a["key_b"] = "value_b"
        a["key_c"] = "value_c"
        check_keys = {"key_a", "key_b", "key_c"}

        for i in a:
            check_keys.remove(i)
        self.assertEqual(set(), check_keys )



    def test_items_iterator(self):
        a = AliasDict()
        a["key_a"] = "value_a"
        a["key_b"] = "value_b"
        a["key_c"] = "value_c"
        for k,v in a.items():
            if k=="key_a":
                self.assertEqual("value_a",v)

            if k=="key_b":
                self.assertEqual("value_b",v)

            if k=="key_c":
                self.assertEqual("value_c",v)

    def test_values(self):
        a = AliasDict()
        a["key_a"] = "value_a"
        a["key_b"] = "value_b"
        a["key_c"] = "value_c"
        check_values = {"value_a", "value_b", "value_c"}
        for v in a.values():
            check_values.remove(v)

        self.assertEqual(set(), check_values )

