import pytest

from cli_pedidos.validators import validar_texto_obrigatorio, validar_valor


@pytest.mark.parametrize("texto", ["10", "10.5", "0.01", "1000"])
def test_validar_valor_aceita_numeros_positivos(texto):
    assert validar_valor(texto) is True


@pytest.mark.parametrize("texto", ["0", "-5", "abc", "", "10abc"])
def test_validar_valor_rejeita_invalidos(texto):
    assert validar_valor(texto) is False


@pytest.mark.parametrize("texto", ["Ana", "  Bruno  ", "x"])
def test_validar_texto_obrigatorio_aceita_preenchido(texto):
    assert validar_texto_obrigatorio(texto) is True


@pytest.mark.parametrize("texto", ["", "   ", None])
def test_validar_texto_obrigatorio_rejeita_vazio(texto):
    assert validar_texto_obrigatorio(texto) is False
