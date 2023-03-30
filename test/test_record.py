import sys
sys.path.append('/home/emb4/sample_system/src')


from little_caret.record.record import Record
import pytest

class TestRecord:
    def test_empty_record(self):
        data = {
            "tako" : [],
            "ika" : [],
        }
        record = Record(data)
        assert record.data == data


    def test_easest_case(self):
        data = {
            "tako" : [1, 2, 3],
            "ika"  : [2, 3, 4],
        }
        record = Record(data)
        assert record.data == data

    # Q01: 下記テストコードを動くように実装を変更せよ
    def test_append(self):
        tako = {
            "tako" : [1, 2, 3],
        }
        ika = {
            "ika"  : [2, 3, 4],
        }
        expect_data = {
            "tako" : [1, 2, 3],
            "ika"  : [2, 3, 4],
        }

        record = Record(tako)
        record.append(ika)
        assert record.data == expect_data

    # Q04: keyが与えられるとそのデータを削除する機能をRecordに実装せよ
    # テストコードから作れ
    # ヒント: Python 辞書型 Keyと調べると何かわかる
    def test_delete(self):
        pass


    # Q06: 凸凹な配列を同じサイズにする関数を実装せよ
    def test_same_size(self):
        data = {
            "tako" : [1, 2, 3, 4, 5],
            "ika"  : [2, 3, 4],
            "kani" : [4, 5, 2, 1],
        }
        expect_data = {
            "tako" : [1, 2, 3, 4, 5],
            "ika"  : [2, 3, 4, 0 ,0],
            "kani" : [4, 5, 2, 1, 0],
        }

        raise NotImplementedError()

    # Q07: データ型がIntではない場合、エラーを出すような実装に変更せよ
    # ヒント: pytest.raises(TypeError)はTypeErrorが発生すると成功と認識する
    def test_different_type_data(self):
        data = {
            "tako" : ["tako1", "tako2"],
        }

        with pytest.raises(TypeError):
            record = Record(data)

    def test_int_data(self):
        data = {
            "ika" : 10,
        }
        expect_data = {
            "ika" : [10],
        }

        record = Record(data)
        assert record.data == expect_data
