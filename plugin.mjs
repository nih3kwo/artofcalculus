function text(value) {
  return { type: 'text', value };
}

function span(value, style) {
  const children = typeof value === 'string' ? [text(value)] : value;
  return { type: 'span', children, style };
}

const styles = [
  { name: 'red', style: { color: '#D44C47', fontWeight: 'bold' } },
  { name: 'green', style: { color: '#448361', fontWeight: 'bold' } },
];

const directives = [];

for (const style of styles) {
  const directive = {
    name: style.name,
    body: { type: String },
    run(data) {
      const text = data.body;
      return [span(text, style.style)];
    },
  };
  directives.push(directive);
}

const plugin = { name: 'Auto Format Directives', roles: directives };

export default plugin;
