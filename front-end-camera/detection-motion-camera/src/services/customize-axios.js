import axios from "axios";

const instance = axios.create({
  // baseURL: 'http://192.168.5.39:8080'
  baseURL: 'http://192.168.1.93:8000/'
});
// Add a request interceptor
instance.interceptors.response.use(function (response) {
  // Do something before request is sent
  return response.data ? response.data:{statusCode: response.status};
}, function (error) {
  // Do something with request error
  return Promise.reject(error);
});

// Add a response interceptor
axios.interceptors.response.use(function (response) {
  // Any status code that lie within the range of 2xx cause this function to trigger
  // Do something with response data
  return response;
}, function (error) {
  // Any status codes that falls outside the range of 2xx cause this function to trigger
  // Do something with response error
  return Promise.reject(error);
});

export default instance;