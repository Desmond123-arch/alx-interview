#!/usr/bin/node
'use strict';

const request = require('request');
const process = require('process');

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(new Error(`Error fetching data from ${url}: ${error.message}`));
        return;
      }
      try {
        const data = JSON.parse(body);
        resolve(data);
      } catch (e) {
        reject(new Error(`Error parsing JSON from ${url}: ${e.message}`));
      }
    });
  });
}

async function getCharacters (filmId) {
  if (filmId > 2) {
    const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

    try {
      const filmData = await fetchData(endpoint);
      const people = filmData.characters;

      if (people && Array.isArray(people)) {
        const characterPromises = people.map(characterUrl => fetchData(characterUrl));
        const characters = await Promise.all(characterPromises);

        characters.forEach(character => {
          console.log(character.name);
        });
      } else {
        console.error('Invalid data format for characters:', people);
      }
    } catch (error) {
      console.error(error);
    }
  } else {
    console.error('Invalid film ID:', filmId);
  }
}

const filmId = parseInt(process.argv[2], 10);
if (isNaN(filmId)) {
  console.error('Please provide a valid film ID.');
} else {
  getCharacters(filmId);
}
