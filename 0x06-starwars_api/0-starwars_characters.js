#!/usr/bin/node
'use strict';

const request = require('request');
const process = require('process');

// Function to fetch data from a URL
function fetchData (url, callback) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error fetching data from ${url}:`, error.message);
      callback(error);
      return;
    }
    try {
      const data = JSON.parse(body);
      callback(null, data);
    } catch (e) {
      console.error(`Error parsing JSON from ${url}:`, e.message);
      callback(e);
    }
  });
}

function getCharacters (filmId) {
  if (filmId > 2) {
    const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

    fetchData(endpoint, (error, data) => {
      if (error) return;

      const people = data.characters;
      if (people && Array.isArray(people)) {
        people.forEach((characterUrl) => {
          fetchData(characterUrl, (err, character) => {
            if (err) return;
            console.log(character.name);
          });
        });
      } else {
        console.error('Invalid data format for characters:', people);
      }
    });
  } else {
    console.error('Invalid film ID:', filmId);
  }
}

// Start the process with the film ID from command-line arguments
const filmId = parseInt(process.argv[2], 10);
if (isNaN(filmId)) {
  console.error('Please provide a valid film ID.');
} else {
  getCharacters(filmId);
}
