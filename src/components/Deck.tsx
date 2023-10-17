import React from 'react';

type PointQuery = string;

enum GameExtension {
  base,
  newleaf,
  pearlbrook,
  spirecrest,
  bellfaire,
  farshore
}

enum CardType {
  traveller,
  production,
  destination,
  governance,
  prosperity
}

enum CardRarity {
  common,
  unique,
  legendary
}

interface Card {
  includedIn: GameExtension
}

interface BaseCard extends Card {
  type: CardType,
  rarity: CardRarity,
  points: number,
  numOfCards: number,
  occupySpace: boolean,
  shareSpaceWith?: Array<BaseCard>,
  related: Array<BaseCard>,
  bonusPoints?: PointQuery,
}

type Critter = BaseCard;
type Construction = BaseCard;

//TODO: implement loading of cards from json