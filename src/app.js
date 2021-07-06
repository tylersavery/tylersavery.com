import "bootstrap";
import "./app.scss";
import "./js/iconography";
import spotlight from "spotlight.js";

import { initEditor } from "./js/editor";
import { wrapRichTextIframes } from "./js/iframe-wrap";

initEditor();
wrapRichTextIframes();
