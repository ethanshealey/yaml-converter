# yaml-converter
This simple application converts a yaml file from tab notation to dot notation

Example:
```yaml
item-1:
    sub-item-1:
        url: https://www.google.com
        index: 0
    sub-item-2:
        url: https://www.youtube.com
        index: 1

item-2:
    sub-item-1:
        deep-item:
            deep-value: Hello World
        deep-item-2:
            sub-deep-item:
                value: true
    sub-item-2: Wow!

```
gets converted to ->
```yaml
item-1.sub-item-1.url: https://www.google.com
item-1.sub-item-1.index: 0
item-1.sub-item-2.url: https://www.youtube.com
item-1.sub-item-2.index: 1

item-2.sub-item-1.deep-item.deep-value: Hello World
item-2.sub-item-1.deep-item-2.sub-deep-item.value: true
item-2.sub-item-2: Wow!
```
