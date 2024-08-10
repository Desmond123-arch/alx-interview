#!/usr/bin/node
'use strict';

const request = require('request');
const process = require('process');

function getPerson (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error fetching person from ${url}:`, error);
      return;
    }
    try {
      const data = JSON.parse(body);
      const person = data.name;
      console.log(person);
    } catch (e) {
      console.error(`Error parsing JSON from ${url}:`, e);
    }
  });
}

if (process.argv.length > 2) {
  const id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error fetching film data from ${url}:`, error);
      return;
    }

    try {
      const data = JSON.parse(body);
      const people = data.characters;

      if (people && Array.isArray(people)) {
        people.forEach(getPerson);
      } else {
        console.error('Invalid data format for characters:', people);
      }
    } catch (e) {
      console.error('Error parsing JSON from film data:', e);
    }
  });
}
