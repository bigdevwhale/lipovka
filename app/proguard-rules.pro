# HMS Core and Huawei Health Kit call into themselves by reflection.
-keepattributes *Annotation*, Exceptions, InnerClasses, Signature
-keep class com.huawei.hms.** { *; }
-keep class com.huawei.hmf.** { *; }
-keep class com.huawei.agconnect.** { *; }
-dontwarn com.huawei.**
# Room entities and DAOs are kept by the Room artifacts' consumer rules.
# Broadcast receivers are referenced from the manifest and kept automatically.
