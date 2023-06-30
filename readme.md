# Password Guesser - Projet en programmation orientée objet Python
Ce projet, appelé Password Guesser, est développé en utilisant le paradigme de la programmation orientée objet (POO) en Python. Le programme vise à générer différentes possibilités de mots de passe en manipulant des mots et des dates.

## Le polymorphisme
Le polymorphisme en programmation orientée objet (POO) est un concept qui permet à des objets de classes différentes de répondre de manière spécifique à une même méthode. En d'autres termes, le polymorphisme permet d'utiliser des objets de différentes classes de manière interchangeable en appelant une méthode commune, mais avec des comportements spécifiques à chaque classe.

Le polymorphisme dans le code ce trouve dans la classe Human month ou la méthode polymorphysme est redéfini car elle existe aussi dans la classe mère Date

## Utilisation de l'encapsulation

L'encapsulation en programmation orientée objet (POO) est un concept qui regroupe les données et les méthodes associées dans une seule entité appelée classe. L'objectif principal de l'encapsulation est de cacher l'implémentation interne de la classe et de fournir un ensemble d'interfaces publiques pour interagir avec l'objet.
L'encapsulation permet de définir les données d'une classe comme des attributs privés, c'est-à-dire qu'ils ne peuvent être accédés directement depuis l'extérieur de la classe. Au lieu de cela, l'accès aux données se fait par des méthodes spéciales appelées accesseurs (getters) et mutateurs (setters). Ces méthodes fournissent une interface contrôlée pour lire et modifier les valeurs des attributs.

L'encapsulation ce trouve dans les constructeurs des classes. Mais en python les préfixe public, private & protected n'existe pas

## Utilisation de la composition
La composition en programmation orientée objet (POO) est un concept qui permet de créer des relations entre les objets où un objet contient d'autres objets en tant que parties composantes. Cela signifie qu'un objet est composé d'autres objets et que la durée de vie de ces objets composants est liée à celle de l'objet conteneur.

## Utilisation de l'héritage
L'héritage en programmation orientée objet (POO) est un mécanisme qui permet à une classe de dériver des propriétés et du comportement d'une autre classe appelée classe parent ou classe de base. La classe dérivée, également appelée classe enfant ou classe dérivée, hérite des attributs (variables) et des méthodes (fonctions) de la classe parent.

L'héritage est plusieurs fois dans le projet, Les classes Leet Lower,Leet Upper,First letter,Strip accents,Uppercase & Lowercase sont des classes filles de Word. Human month est une classe fille de Date

## Interface
En programmation orientée objet (POO), une interface est une spécification abstraite d'un ensemble de méthodes qu'une classe doit implémenter. Elle définit un contrat que les classes doivent respecter lorsqu'elles prétendent implémenter cette interface. En d'autres termes, une interface définit les méthodes qu'une classe doit fournir, mais ne spécifie pas comment elles doivent être implémentées.

Dans le code DateInterface est l'interface de la class Date

## Utilisation de méthodes et attributs d'objets
L'utilisation de méthodes et attributs d'objets en programmation orientée objet (POO) fait référence à l'accès et à l'utilisation des fonctionnalités fournies par les objets d'une classe.
Une classe est une structure de programmation qui définit un ensemble de comportements et d'attributs communs à un groupe d'objets. Chaque objet créé à partir de cette classe possède ses propres attributs et peut exécuter des méthodes spécifiques définies dans la classe.

## Utilisation de méthodes et attributs statiques
L'utilisation de méthodes et attributs statiques en programmation orientée objet (POO) fait référence à l'accès et à l'utilisation de fonctionnalités qui sont associées à la classe elle-même plutôt qu'à une instance spécifique de la classe.
Dans la POO, une méthode statique est une méthode qui est définie au niveau de la classe plutôt qu'au niveau de l'objet. Elle peut être invoquée directement sur la classe elle-même, sans nécessiter la création d'une instance de la classe. Les méthodes statiques sont souvent utilisées pour implémenter des fonctionnalités utilitaires ou des opérations qui ne dépendent pas de l'état spécifique de l'objet.

## Utilisation de méthodes et attributs de classe
L'utilisation de méthodes et attributs de classe en programmation orientée objet (POO) fait référence à l'accès et à l'utilisation de fonctionnalités qui sont associées à la classe elle-même plutôt qu'à une instance spécifique de la classe.
Les méthodes de classe, également appelées méthodes statiques liées à la classe, sont des méthodes qui agissent sur la classe dans son ensemble plutôt que sur une instance particulière de la classe. Elles sont définies au niveau de la classe et utilisent souvent les attributs de classe pour effectuer des opérations. Les méthodes de classe sont généralement utilisées pour implémenter des fonctionnalités qui sont liées à la classe en tant qu'entité globale, mais qui ne nécessitent pas l'accès aux attributs spécifiques des instances.

Voici un exemple dans le code de méthode de classe
