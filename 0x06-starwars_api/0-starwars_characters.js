#!/usr/bin/node
'use strict';

const request = require('request');

require('process');

function getPerson (url) {
  request(url, (error, response, body) => {
    if (error) console.log(error);
    try {
      const data = JSON.parse(body);
      const person = data.name;
      console.log(person);
    } catch (e) {
      console.log(e);
    }
  });
}

let people;
if (process.argv.length > 2) {
  const id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';
  console.log(url);
  request(url, (error, response, body) => {
    if (error) console.log(error);

    try {
      const data = JSON.parse(body);
      people = data.characters;
      people.map(getPerson);
    } catch (e) {
      console.log(e);
    }
  });
}
