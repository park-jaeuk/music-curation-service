/* eslint-disable @typescript-eslint/no-explicit-any */
import axios, { AxiosRequestConfig } from "axios";

export const BASE_URL = "http://34.47.108.61:8000";

const instance = axios.create({
  headers: { "Content-Type": "application/json" },
});

export const api = {
  get: async <T>(path: string, options?: AxiosRequestConfig | undefined) =>
    (await instance.get<T>(path, options)).data,
  put: async <T>(path: string, options?: AxiosRequestConfig | undefined) =>
    (await instance.put<T>(path, options)).data,
  delete: async <T>(path: string, options?: AxiosRequestConfig | undefined) =>
    (await instance.delete<T>(path, options)).data,
  post: async <T>(
    path: string,
    data: any,
    options?: AxiosRequestConfig | undefined
  ) => (await instance.post<T>(path, data, options)).data,
  patch: async <T>(
    path: string,
    data: any,
    options?: AxiosRequestConfig | undefined
  ) => (await instance.patch<T>(path, data, options)).data,
};
