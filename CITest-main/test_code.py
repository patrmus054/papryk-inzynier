from main import dodawanie, potega2

def test_pass():
	assert 1 + 1 == 2

def test_dodawanie():
	assert dodawanie(2,4) == 6

def test_potega2():
	assert potega2(5) == 25
