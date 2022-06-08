import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '30s',
};

export default function() {
  // host = process.env.get('HOST', 'localhost');
  // port = porcess.env.get('PORT', '8080');
  //
  // console.log(`Conecting against: http://${host}:${port}/`);
  // http.get(`http://${host}:${port}/`);
  http.get(`http://localhost:8080/`);
  sleep(1);
}
