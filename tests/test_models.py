from src.models import Conta

def test_verificar_se_o_saldo_inicial_e_igual_a_zero():
    c1 = Conta(1)
    assert 0.0 == c1.saldo()

def test_verificar_se_o_saldo_atualiza_conforme_o_deposito():
    c1 = Conta(1)
    c1.depositar(200.00)
    assert 200.00 == c1.saldo()
    c1.depositar(50.00)
    assert 250.00 == c1.saldo()

def test_verificar_se_o_saldo_atualiza_conforme_o_saque():
    c1 = Conta(1)
    c1.sacar(50.00)
    assert -50.0 == c1.saldo()

def test_verificar_se_o_limite_e_utilizado_para_saque():
    c2 = Conta(2)
    c2.sacar(10.00)
    assert -10.00 == c2.saldo()