"""Tests for graph builder module."""

import pytest


def test_import_graph_builder():
    """Test that graph builder can be imported."""
    from codemap.core.graph_builder import GraphBuilder

    assert GraphBuilder is not None


def test_graph_builder_initialization():
    """Test GraphBuilder can be initialized."""
    from codemap.core.graph_builder import GraphBuilder

    builder = GraphBuilder()
    assert builder is not None
    assert hasattr(builder, "entities")
    assert hasattr(builder, "relationships")


def test_graph_builder_has_entities_dict():
    """Test GraphBuilder has entities dictionary."""
    from codemap.core.graph_builder import GraphBuilder

    builder = GraphBuilder()
    assert isinstance(builder.entities, dict)
    assert len(builder.entities) == 0


def test_graph_builder_build_networkx():
    """Test GraphBuilder can build a NetworkX graph."""
    from codemap.core.graph_builder import GraphBuilder

    builder = GraphBuilder()
    # Build graph with empty data - should return a graph object
    try:
        G = builder.build_networkx()
        assert G is not None
        assert hasattr(G, "nodes")
        assert hasattr(G, "edges")
    except ImportError:
        # networkx might not be installed in test env
        pytest.skip("networkx not installed")
