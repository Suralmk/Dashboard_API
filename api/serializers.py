from rest_framework import serializers
from . models import Statstics
import datetime
from django.db.models import Sum
class IntensitySerializer(serializers.Serializer):
    intensity = serializers.IntegerField()


class StatsticsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statstics
        fields = "__all__"

class AddstatsticsDataSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Statstics
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        try:
            title = validated_data.get("title") or None
            country =validated_data.get("country") or None
            source = validated_data.get("source") or None
            pestle = validated_data.get("pestle") or None
            region = validated_data.get("region") or None 
            topic = validated_data.get("topic")   or None 
            topic = validated_data.get("topic")  or None 
            sector =validated_data.get("sector") or None 
            insight = validated_data.get("title") or None 
            impact =validated_data.get("impact") or None 
            start_year =validated_data.get("start_year") or None 
            end_year =validated_data.get("end_year") or None 
            published = validated_data.get("published") or None 
            added = validated_data.get("added") or None 
            relevance = validated_data.get("relevance") or None 
            intensity = validated_data.get("intensity") or None 
            likelihood = validated_data.get("likelihood") or None 
            url = validated_data.get("url") or None 
            stats = Statstics.objects.create(title=title, insight=insight,country=country, source=source, pestle=pestle, region=region, topic=topic, sector=sector, impact=impact, start_year=start_year, end_year=end_year, published=published, added=added, relevance=relevance, intensity=intensity, likelihood=likelihood, url=url)
            return True
        except Exception as e:
            print(e)

class DashboardDataSerializer(serializers.Serializer):
    sector_ril = serializers.SerializerMethodField()
    sector_intensity = serializers.SerializerMethodField()
    region_intensity = serializers.SerializerMethodField()
    topic_intensity = serializers.SerializerMethodField()
    country_intensity = serializers.SerializerMethodField()
    topic_relevance= serializers.SerializerMethodField()
    topic_ril = serializers.SerializerMethodField()
    region_ril = serializers.SerializerMethodField()

    def get_region_ril(self, obj):
        relevance = Statstics.objects.values("region").annotate(Sum("relevance"))
        rel = [x["relevance__sum"] for x in relevance if  x["region"] is not None]

        likelihood = Statstics.objects.values("region").annotate(Sum("likelihood"))
        like = [x["likelihood__sum"] for x in likelihood if x["region"] is not None ]

        intensity = Statstics.objects.values("region").annotate(Sum("intensity"))
        inten = [x["intensity__sum"] for x in intensity if x["region"] is not None ]

        label = [x["region"] for x in relevance if x["region"] is not None]
        return {
            "data": {
                "relevance": rel,
                "likelihood": like,
                "intensity": inten,
            }, "labels" :label
       
        }

    def get_sector_ril(self, obj):
        relevance = Statstics.objects.values("sector").annotate(Sum("relevance"))
        rel = [x["relevance__sum"] for x in relevance if  x["sector"] is not None]

        likelihood = Statstics.objects.values("sector").annotate(Sum("likelihood"))
        like = [x["likelihood__sum"] for x in likelihood if x["sector"] is not None ]

        intensity = Statstics.objects.values("sector").annotate(Sum("intensity"))
        inten = [x["intensity__sum"] for x in intensity if x["sector"] is not None ]

        label = [x["sector"] for x in relevance if x["sector"] is not None]
        return {
            "data": {
                "relevance": rel,
                "likelihood": like,
                "intensity": inten,
            }, "labels" :label
       
        }

    def get_topic_ril(self, obj):
        relevance = Statstics.objects.values("topic").annotate(Sum("relevance"))
        rel = [x["relevance__sum"] for x in relevance if  x["topic"] is not None]

        likelihood = Statstics.objects.values("topic").annotate(Sum("likelihood"))
        like = [x["likelihood__sum"] for x in likelihood if x["topic"] is not None ]

        intensity = Statstics.objects.values("topic").annotate(Sum("intensity"))
        inten = [x["intensity__sum"] for x in intensity if x["topic"] is not None ]

        label = [x["topic"] for x in relevance if x["topic"] is not None]
        return {
            "data": {
                "relevance": rel,
                "likelihood": like,
                "intensity": inten,
            }, "labels" :label
       
        }

    def get_sector_intensity(self, onj):
        cdata = Statstics.objects.all().values("sector").annotate(Sum("intensity"))
        label = [x["sector"] for x in cdata if x["sector"] is not None]
        data = [x["intensity__sum"] for x in cdata if x["sector"] is not None]
        return  {
            "labels" : label,
            "data":data
        }
    
    def get_region_intensity(self, obj):
        cdata = Statstics.objects.all().values("region").annotate(Sum("intensity"))
        label = [x["region"] for x in cdata if x["region"] is not None]
        data = [x["intensity__sum"] for x in cdata if x["region"] is not None]
        return {
            "labels" : label,
            "data":data
        }

    def get_topic_intensity(self, obj):
        cdata = Statstics.objects.all().values("topic").annotate(Sum("intensity"))
        label = [x["topic"] for x in cdata if x["topic"] is not None]
        data = [x["intensity__sum"] for x in cdata if x["topic"] is not None]
        return {
            "labels" : label,
            "data":data
        }

    def get_country_intensity(self, obj):
        cdata = Statstics.objects.all().values("country").annotate(Sum("intensity"))
        label = [x["country"] for x in cdata if x["country"] is not None]
        data = [x["intensity__sum"] for x in cdata if x["country"] is not None]
        return {
            "labels" : label,
            "data":data
        }

    def get_topic_relevance(self, obj):
        cdata = Statstics.objects.all().values("topic").annotate(Sum("relevance"))
        label = [x["topic"] for x in cdata if x["topic"] is not None]
        data = [x["relevance__sum"] for x in cdata if x["topic"] is not None]
        return {
            "labels" : label,
            "data":data
        }
        