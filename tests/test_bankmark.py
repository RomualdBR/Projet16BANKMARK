import unittest
from bankmark.texte import analyser_modalites

class TestAnalyseModalites(unittest.TestCase):

    def test_analyser_modalites_nominal(self):
        # Test avec un format standard issu du codebook
        texte = "no:Non; yes: Oui"
        attendu = {'no': 'Non', 'yes': 'Oui'}
        self.assertEqual(analyser_modalites(texte), attendu)

    def test_analyser_modalites_multiples(self):
        # Test avec plusieurs modalités et des espaces variés
        texte = "married: Marié; single: Célibataire; divorced: Divorcé ou veuf"
        attendu = {
            'married': 'Marié',
            'single': 'Célibataire',
            'divorced': 'Divorcé ou veuf'
        }
        self.assertEqual(analyser_modalites(texte), attendu)

    def test_analyser_modalites_erreur(self):
        # Test du cas d'erreur : absence de deux-points ':'
        texte_invalide = "no:Non; erreur_sans_deux_points; yes: Oui"
        with self.assertRaises(ValueError):
            analyser_modalites(texte_invalide)

if __name__ == '__main__':
    unittest.main()