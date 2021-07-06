function wrap(element) {
    var wrapper = document.createElement("div");
    wrapper.className = "embed-responsive embed-responsive-16by9";
    element.parentNode.insertBefore(wrapper, element);
    wrapper.appendChild(element);
    return wrapper;
}

export function wrapRichTextIframes() {
    document
        .querySelectorAll(".block-rich_text iframe")
        .forEach((iframe) => wrap(iframe));
}
