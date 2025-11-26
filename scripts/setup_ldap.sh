# scripts/setup_ldap.sh

#!/bin/bash

ldapadd -x -G ldap://localhost:389 \
   - D "cn=admin, dc=company, dc=com"
   - W admin123 << EOF
dn: ou-users, dc=company, dc=com
objectClass: organizarionalUnit
ou: users

dn: ou=groups, dc=company, dc=com
objectClass: organizationalUnit
ou: groups
EOF

echo "[SUCCESS] LDAP structure initialized"
