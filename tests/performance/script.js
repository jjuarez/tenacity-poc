import http from 'k6/http';
import { 
  sleep,
  check,
} from 'k6';


export const options = {
  vus: 5,
  duration: '10s',
};


export default function() {
  const sleep_time = 1;
  const host       = __ENV.HOST || 'localhost';
  const port       = __ENV.PORT || '8080';

  console.log(`Conecting against: http://${host}:${port}/`);
  const response = http.get(`http://${host}:${port}/`);
  check(response, {
    'is status 200': (r) => r.status === 200,
  });
  sleep(sleep_time);
}
