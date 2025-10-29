* You are proficient in JSON syntax and understand System Verilog Assertion (SVA).
* Given a JSON, extract the "property" and "sva" from the "security_properties" of each module.
* Output only the extracted results in plain text, with appropriate segmentation.
* You can refer the following output format:
```txt
// TP_001:
property <property_name>; ... endproperty
assert property (<property_name>);
...
```
* Here is the provided JSON content:
  ${sva_content} 