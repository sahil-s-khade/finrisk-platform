import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000/api/v1",
});

export const loginUser = async () => {
  const response = await API.post("/login", {
    username: "admin",
    password: "admin123",
  });

  return response.data.access_token;
};

export default API;