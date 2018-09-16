import reducers from "./reducers";
import { createLogger } from "redux-logger";
import { createStore, applyMiddleware } from "redux";
import thunkMiddleware from "redux-thunk";


const loggerMiddleware = createLogger();
const store = createStore(
	reducers,
	applyMiddleware(
		thunkMiddleware,
		loggerMiddleware,
	)
);

export { store }
