import pytest

class TestGetBwWeight:
    def test_g_weight(self):
        bw_weights = {'Wgd': 0.5, 'Wgg': 0.3}
        assert get_bw_weight('g', 'guard', bw_weights) == 0.5
        assert get_bw_weight('g', 'exit', bw_weights) == 0.3

    def test_m_weight(self):
        bw_weights = {'Wmd': 0.2, 'Wme': 0.8}
        assert get_bw_weight('m', 'intro', bw_weights) == 0.2
        assert get_bw_weight('m', 'exit', bw_weights) == 0.8

    def test_e_weight(self):
        bw_weights = {'Wed': 0.1, 'Wee': 0.9}
        assert get_bw_weight('e', 'guard', bw_weights) == 0.1
        assert get_bw_weight('e', 'exit', bw_weights) == 0.9

    def test_h2_weight(self):
        bw_weights = {'Wem': 0.5, 'Wee': 0.5}
        assert get_bw_weight('h2', 'guard', bw_weights) == 1.0
        assert get_bw_weight('h2', 'exit', bw_weights) == 0.5

    def test_h3_weight(self):
        bw_weights = {'Wem': 0.5, 'Wee': 0.5}
        assert get_bw_weight('h3', 'guard', bw_weights) == 1.0
        assert get_bw_weight('h3', 'exit', bw_weights) == 0.5

    def test_stable_weight(self):
        bw_weights = {'Wmm': 0.2, 'Wmg': 0.8}
        assert get_bw_weight('stable', 'intro', bw_weights) == 0.2
        assert get_bw_weight('stable', 'exit', bw_weights) == 0.8

    def test_exit_flagged_nodes(self):
        bw_weights = {'Wgd': 0.5, 'Wgg': 0.3}
        with pytest.raises(ValueError):
            get_bw_weight('g', 'guard', bw_weights)

    def test_position_not_supported(self):
        bw_weights = {'Wmd': 0.2, 'Wee': 0.8}
        with pytest.raises(ValueError):
            get_bw_weight('h1', 'intro', bw_weights)
