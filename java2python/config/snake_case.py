from java2python.lang.selector import *

astTransforms = [
	(Type('NULL'),  transform.null2None),
	(Type('FALSE'), transform.false2False),
	(Type('TRUE'),  transform.true2True),
#(Type('IDENT'), transform.keywordSafeIdent),
	(Type('IDENT'),camel_to_snake),

	(Type('FLOATING_POINT_LITERAL'), transform.syntaxSafeFloatLiteral),

	(Type('TYPE') > Type('BOOLEAN'), transform.typeSub),
	(Type('TYPE') > Type('BYTE'), transform.typeSub),
	(Type('TYPE') > Type('CHAR'), transform.typeSub),
	(Type('TYPE') > Type('FLOAT'), transform.typeSub),
	(Type('TYPE') > Type('INT'), transform.typeSub),
	(Type('TYPE') > Type('SHORT'), transform.typeSub),
	(Type('TYPE') > Type('LONG'), transform.typeSub),
	(Type('TYPE') > Type('DOUBLE'), transform.typeSub),

	(Type('METHOD_CALL') > Type('DOT') > Type('IDENT', 'length'),
	 transform.lengthToLen),

	(Type('METHOD_CALL') > Type('DOT') > (
										  Type('IDENT', 'String') +
										  Type('IDENT', 'format')
										 ),
	 transform.formatString),

	(Type('TYPE') > Type('QUALIFIED_TYPE_IDENT') > Type('IDENT'),
	 transform.typeSub),
	
	(Type('FUNCTIION_METHOD_DECL') > Type('IDENT'),camel_to_snake),
	(Type('VOID_METHOD_DECL') > Type('IDENT'),camel_to_snake)
]
