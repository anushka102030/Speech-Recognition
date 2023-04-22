import { render, screen } from '@testing-library/react';
import App from './App';

import {rest} from "msw";
import {setupServer } from "msw/node";

const response = rest.get("./test_data.json", (req, res, ctx) => {
  return res(ctx.json([{message: "successful response"}]));
});

const server = new setupServer(response);



beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test('renders page with successful request output', async () => {
  render(<App />);
  const linkElement = await screen.findByText("successful response");
  expect(linkElement).toBeVisible();
});
