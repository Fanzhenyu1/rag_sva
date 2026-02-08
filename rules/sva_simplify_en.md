* You are proficient in JSON syntax and understand System Verilog Assertion (SVA).
* Given a JSON, extract the "property" and "sva" from the "security_properties" of each module.
* Output only the extracted results in system verilog format, with appropriate segmentation.
* You can refer the following output format:
```sv
// TP_001:
property <property_name>;
  ...
endproperty
assert property (<property_name>);
...
```
* Here is the provided JSON content:
{sva_content} 